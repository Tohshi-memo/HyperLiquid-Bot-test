# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T14:37:27.290881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `13`; crypto_alt avg `0.1108` n `235`; crypto_major avg `0.0702` n `8`; equity avg `0.1472` n `150`; fx avg `0.0037` n `6`; index avg `0.0068` n `26`; metal avg `0.001` n `20`; unknown avg `0.2031` n `1078`
- 1h: commodity avg `0.2334` n `13`; crypto_alt avg `0.3282` n `235`; crypto_major avg `0.4927` n `8`; equity avg `-0.0571` n `150`; fx avg `0.0136` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0283` n `20`; unknown avg `0.0571` n `1028`
- 4h: commodity avg `0.469` n `13`; crypto_alt avg `0.0794` n `235`; crypto_major avg `0.1421` n `8`; equity avg `-0.3802` n `150`; fx avg `-0.0273` n `6`; index avg `-0.0642` n `26`; metal avg `0.0729` n `20`; unknown avg `1.3632` n `1022`
- 24h: commodity avg `0.0816` n `13`; crypto_alt avg `-1.5973` n `235`; crypto_major avg `-1.1373` n `8`; equity avg `-0.7651` n `150`; fx avg `-0.0203` n `6`; index avg `-0.0862` n `26`; metal avg `0.5604` n `20`; unknown avg `30.2441` n `955`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
