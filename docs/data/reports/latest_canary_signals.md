# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T14:07:27.888494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.134` n `231`; crypto_major avg `0.0415` n `8`; equity avg `0.0054` n `127`; fx avg `-0.0033` n `6`; index avg `-0.0018` n `26`; metal avg `0.0011` n `20`; unknown avg `0.0527` n `793`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.4078` n `231`; crypto_major avg `0.2158` n `8`; equity avg `0.0424` n `127`; fx avg `-0.0071` n `6`; index avg `-0.0024` n `26`; metal avg `0.0053` n `20`; unknown avg `0.0114` n `793`
- 4h: commodity avg `0.0091` n `12`; crypto_alt avg `0.5758` n `231`; crypto_major avg `0.4039` n `8`; equity avg `-0.0152` n `127`; fx avg `-0.0117` n `6`; index avg `-0.0012` n `26`; metal avg `0.0039` n `20`; unknown avg `0.093` n `761`
- 24h: commodity avg `0.1549` n `12`; crypto_alt avg `-0.6839` n `231`; crypto_major avg `-1.1356` n `8`; equity avg `-0.6981` n `127`; fx avg `-0.0324` n `6`; index avg `-0.1119` n `26`; metal avg `-0.498` n `20`; unknown avg `-0.3099` n `743`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2023`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
