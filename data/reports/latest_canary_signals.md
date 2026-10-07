# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T22:07:32.569760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1199` n `13`; crypto_alt avg `0.2632` n `235`; crypto_major avg `0.1603` n `8`; equity avg `0.031` n `150`; fx avg `-0.0122` n `6`; index avg `0.0264` n `26`; metal avg `-0.0193` n `20`; unknown avg `0.0051` n `1075`
- 1h: commodity avg `0.1128` n `13`; crypto_alt avg `-0.1875` n `235`; crypto_major avg `-0.2722` n `8`; equity avg `0.0604` n `150`; fx avg `-0.0116` n `6`; index avg `0.0235` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.2384` n `1075`
- 4h: commodity avg `0.5355` n `13`; crypto_alt avg `0.2195` n `235`; crypto_major avg `-0.1695` n `8`; equity avg `0.0234` n `150`; fx avg `0.0239` n `6`; index avg `0.0143` n `26`; metal avg `-0.0831` n `20`; unknown avg `0.5256` n `999`
- 24h: commodity avg `0.5129` n `13`; crypto_alt avg `-4.2915` n `235`; crypto_major avg `-3.6767` n `8`; equity avg `-1.3978` n `150`; fx avg `-0.1501` n `6`; index avg `-0.2089` n `26`; metal avg `-0.699` n `20`; unknown avg `247.5348` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
