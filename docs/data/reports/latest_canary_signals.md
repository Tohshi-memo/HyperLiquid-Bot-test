# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T04:37:24.675718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `13`; crypto_alt avg `-0.0697` n `237`; crypto_major avg `-0.0214` n `8`; equity avg `-0.0279` n `151`; fx avg `-0.0138` n `6`; index avg `-0.019` n `26`; metal avg `-0.0133` n `20`; unknown avg `-0.0575` n `1196`
- 1h: commodity avg `-0.0121` n `13`; crypto_alt avg `0.2126` n `237`; crypto_major avg `0.2189` n `8`; equity avg `-0.3422` n `151`; fx avg `-0.0203` n `6`; index avg `-0.0736` n `26`; metal avg `-0.0045` n `20`; unknown avg `0.4612` n `1188`
- 4h: commodity avg `0.0728` n `13`; crypto_alt avg `0.8091` n `237`; crypto_major avg `0.5341` n `8`; equity avg `-0.1531` n `151`; fx avg `0.0057` n `6`; index avg `-0.0764` n `26`; metal avg `0.1338` n `20`; unknown avg `1.473` n `1188`
- 24h: commodity avg `0.2681` n `13`; crypto_alt avg `0.8863` n `237`; crypto_major avg `-0.0543` n `8`; equity avg `-1.0789` n `151`; fx avg `-0.0456` n `6`; index avg `-0.1997` n `26`; metal avg `-0.2139` n `20`; unknown avg `5.3423` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
