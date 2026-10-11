# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T10:52:27.139735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `-0.0082` n `235`; crypto_major avg `0.0463` n `8`; equity avg `-0.0079` n `150`; fx avg `0.0014` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.4976` n `1117`
- 1h: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.369` n `235`; crypto_major avg `-0.0768` n `8`; equity avg `-0.0125` n `150`; fx avg `0.0059` n `6`; index avg `0.0009` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.6041` n `1115`
- 4h: commodity avg `0.0099` n `13`; crypto_alt avg `-0.6149` n `235`; crypto_major avg `-0.2791` n `8`; equity avg `0.0101` n `150`; fx avg `0.0008` n `6`; index avg `0.0068` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.2677` n `1099`
- 24h: commodity avg `0.4436` n `13`; crypto_alt avg `0.8265` n `235`; crypto_major avg `-0.1323` n `8`; equity avg `0.0819` n `150`; fx avg `-0.0044` n `6`; index avg `-0.0049` n `26`; metal avg `0.0006` n `20`; unknown avg `1.0368` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
