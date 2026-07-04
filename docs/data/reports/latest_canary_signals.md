# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T08:13:18.809985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `-0.0279` n `229`; crypto_major avg `-0.0049` n `8`; equity avg `-0.0122` n `88`; fx avg `-0.0049` n `6`; index avg `0.003` n `25`; metal avg `0.0056` n `20`; unknown avg `0.2028` n `765`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `-0.0748` n `229`; crypto_major avg `0.2141` n `8`; equity avg `-0.0366` n `88`; fx avg `-0.024` n `6`; index avg `-0.0218` n `25`; metal avg `0.0167` n `20`; unknown avg `0.5463` n `765`
- 4h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.5351` n `229`; crypto_major avg `-0.2374` n `8`; equity avg `-0.002` n `88`; fx avg `-0.0117` n `6`; index avg `-0.0121` n `25`; metal avg `0.0167` n `20`; unknown avg `0.4052` n `745`
- 24h: commodity avg `-0.0566` n `12`; crypto_alt avg `1.5255` n `229`; crypto_major avg `2.314` n `8`; equity avg `0.3105` n `88`; fx avg `-0.0447` n `6`; index avg `-0.0469` n `25`; metal avg `-0.2251` n `20`; unknown avg `5.3886` n `733`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
