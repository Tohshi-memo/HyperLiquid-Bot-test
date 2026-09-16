# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T20:22:29.712608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8519` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8226` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `0.1588` n `234`; crypto_major avg `0.1157` n `8`; equity avg `0.052` n `137`; fx avg `0.0096` n `6`; index avg `0.002` n `27`; metal avg `-0.0267` n `20`; unknown avg `5.4231` n `891`
- 1h: commodity avg `-0.04` n `12`; crypto_alt avg `1.0082` n `234`; crypto_major avg `1.1661` n `8`; equity avg `1.1163` n `137`; fx avg `0.052` n `6`; index avg `0.185` n `27`; metal avg `0.1504` n `20`; unknown avg `4.9028` n `867`
- 4h: commodity avg `-0.0469` n `12`; crypto_alt avg `1.2943` n `234`; crypto_major avg `1.2821` n `8`; equity avg `-0.5405` n `137`; fx avg `0.0616` n `6`; index avg `-0.2076` n `27`; metal avg `-0.5698` n `20`; unknown avg `5.2192` n `829`
- 24h: commodity avg `-0.6311` n `12`; crypto_alt avg `0.0996` n `234`; crypto_major avg `1.2346` n `8`; equity avg `0.7558` n `137`; fx avg `0.0902` n `6`; index avg `0.0113` n `27`; metal avg `-0.2931` n `20`; unknown avg `1.8002` n `771`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
