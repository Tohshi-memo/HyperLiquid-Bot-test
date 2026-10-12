# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T09:22:32.840420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `13`; crypto_alt avg `-0.128` n `235`; crypto_major avg `-0.0779` n `8`; equity avg `0.0099` n `151`; fx avg `-0.0122` n `6`; index avg `0.0157` n `26`; metal avg `0.0252` n `20`; unknown avg `-0.009` n `1109`
- 1h: commodity avg `0.1274` n `13`; crypto_alt avg `-0.0916` n `235`; crypto_major avg `-0.1187` n `8`; equity avg `-0.2444` n `151`; fx avg `-0.011` n `6`; index avg `-0.0535` n `26`; metal avg `0.0116` n `20`; unknown avg `0.1603` n `1067`
- 4h: commodity avg `0.3182` n `13`; crypto_alt avg `-0.9739` n `235`; crypto_major avg `-0.6906` n `8`; equity avg `-0.7475` n `151`; fx avg `-0.0598` n `6`; index avg `-0.0995` n `26`; metal avg `-0.0284` n `20`; unknown avg `0.4909` n `1007`
- 24h: commodity avg `-0.1224` n `13`; crypto_alt avg `2.0125` n `235`; crypto_major avg `1.3224` n `8`; equity avg `-1.055` n `151`; fx avg `-0.1121` n `6`; index avg `-0.1125` n `26`; metal avg `0.0068` n `20`; unknown avg `0.1646` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
