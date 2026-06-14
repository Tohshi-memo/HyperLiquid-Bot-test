# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T05:52:32.664576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `0.3528` n `228`; crypto_major avg `0.1474` n `8`; equity avg `0.0134` n `74`; fx avg `0.0097` n `6`; index avg `0.0141` n `23`; metal avg `0.2044` n `18`; unknown avg `1.6225` n `645`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `0.1344` n `228`; crypto_major avg `0.0063` n `8`; equity avg `0.0097` n `74`; fx avg `0.0073` n `6`; index avg `-0.0107` n `23`; metal avg `0.0145` n `18`; unknown avg `0.9511` n `645`
- 4h: commodity avg `-0.037` n `12`; crypto_alt avg `-0.5175` n `228`; crypto_major avg `-0.433` n `8`; equity avg `-0.0097` n `74`; fx avg `0.0104` n `6`; index avg `-0.0511` n `23`; metal avg `0.0082` n `18`; unknown avg `-0.8334` n `629`
- 24h: commodity avg `-0.7187` n `12`; crypto_alt avg `1.8129` n `228`; crypto_major avg `1.841` n `8`; equity avg `0.811` n `74`; fx avg `-0.0281` n `6`; index avg `0.2067` n `23`; metal avg `0.3357` n `18`; unknown avg `-1.0412` n `603`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
