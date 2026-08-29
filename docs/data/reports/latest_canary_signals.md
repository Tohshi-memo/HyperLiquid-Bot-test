# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T07:37:28.783241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `0.0348` n `231`; crypto_major avg `0.0308` n `8`; equity avg `0.0105` n `127`; fx avg `-0.0042` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.0108` n `793`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `0.1135` n `231`; crypto_major avg `0.1211` n `8`; equity avg `0.0561` n `127`; fx avg `-0.0039` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.0248` n `793`
- 4h: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.1132` n `231`; crypto_major avg `-0.1381` n `8`; equity avg `0.1113` n `127`; fx avg `0.0003` n `6`; index avg `0.014` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0582` n `761`
- 24h: commodity avg `0.0098` n `12`; crypto_alt avg `-1.8376` n `231`; crypto_major avg `-2.4692` n `8`; equity avg `-1.4904` n `127`; fx avg `-0.0132` n `6`; index avg `-0.1483` n `26`; metal avg `-0.6303` n `20`; unknown avg `-0.3426` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
