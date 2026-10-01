# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T22:52:27.210034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.1376` n `234`; crypto_major avg `-0.1317` n `8`; equity avg `-0.0016` n `142`; fx avg `-0.0067` n `6`; index avg `0.0021` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.1002` n `985`
- 1h: commodity avg `-0.0654` n `13`; crypto_alt avg `0.1002` n `234`; crypto_major avg `0.2158` n `8`; equity avg `0.0832` n `142`; fx avg `-0.0041` n `6`; index avg `0.007` n `26`; metal avg `-0.0089` n `20`; unknown avg `0.3838` n `967`
- 4h: commodity avg `0.0289` n `13`; crypto_alt avg `-0.5349` n `234`; crypto_major avg `-0.2723` n `8`; equity avg `0.01` n `142`; fx avg `0.0077` n `6`; index avg `0.0086` n `26`; metal avg `0.047` n `20`; unknown avg `-0.2505` n `891`
- 24h: commodity avg `0.1307` n `13`; crypto_alt avg `-0.9968` n `234`; crypto_major avg `-0.5235` n `8`; equity avg `0.9294` n `142`; fx avg `-0.1` n `6`; index avg `0.1584` n `26`; metal avg `-0.0148` n `20`; unknown avg `-0.0173` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
