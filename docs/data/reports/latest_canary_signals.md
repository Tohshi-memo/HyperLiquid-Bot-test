# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T15:17:50.337850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `0.048` n `234`; crypto_major avg `0.0832` n `8`; equity avg `-0.0196` n `138`; fx avg `-0.0074` n `6`; index avg `0.0061` n `26`; metal avg `0.0485` n `20`; unknown avg `-0.0097` n `919`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.7614` n `234`; crypto_major avg `-0.6278` n `8`; equity avg `-0.0761` n `138`; fx avg `-0.0176` n `6`; index avg `-0.0199` n `26`; metal avg `-0.08` n `20`; unknown avg `0.5043` n `915`
- 4h: commodity avg `0.0979` n `12`; crypto_alt avg `0.2739` n `234`; crypto_major avg `0.6624` n `8`; equity avg `0.4349` n `138`; fx avg `-0.042` n `6`; index avg `0.1197` n `26`; metal avg `0.2044` n `20`; unknown avg `1.0682` n `891`
- 24h: commodity avg `-0.1079` n `12`; crypto_alt avg `4.0969` n `234`; crypto_major avg `2.2829` n `8`; equity avg `1.2152` n `138`; fx avg `0.0396` n `6`; index avg `0.1644` n `26`; metal avg `0.1337` n `20`; unknown avg `0.3782` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
