# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T11:37:26.460197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0438` n `231`; crypto_major avg `-0.0383` n `8`; equity avg `0.0033` n `127`; fx avg `-0.0014` n `6`; index avg `0.0073` n `26`; metal avg `0.0104` n `20`; unknown avg `0.2789` n `789`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.0363` n `231`; crypto_major avg `-0.0373` n `8`; equity avg `0.01` n `127`; fx avg `0.0` n `6`; index avg `0.0112` n `26`; metal avg `0.0124` n `20`; unknown avg `0.0931` n `775`
- 4h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.3722` n `231`; crypto_major avg `-0.0446` n `8`; equity avg `0.0074` n `127`; fx avg `-0.0095` n `6`; index avg `0.0019` n `26`; metal avg `0.0186` n `20`; unknown avg `0.0379` n `773`
- 24h: commodity avg `0.0628` n `12`; crypto_alt avg `-2.4475` n `231`; crypto_major avg `-2.2641` n `8`; equity avg `-1.367` n `127`; fx avg `-0.0888` n `6`; index avg `-0.1257` n `26`; metal avg `-0.7189` n `20`; unknown avg `-0.2846` n `756`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
