# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T13:07:36.229474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0738` n `12`; crypto_alt avg `-0.0688` n `229`; crypto_major avg `-0.0339` n `8`; equity avg `-0.0848` n `91`; fx avg `-0.0066` n `6`; index avg `-0.0244` n `25`; metal avg `0.0428` n `20`; unknown avg `-0.1268` n `766`
- 1h: commodity avg `-0.2407` n `12`; crypto_alt avg `-0.0203` n `229`; crypto_major avg `-0.1689` n `8`; equity avg `-0.0193` n `91`; fx avg `-0.0254` n `6`; index avg `0.0115` n `25`; metal avg `0.0508` n `20`; unknown avg `-0.1731` n `766`
- 4h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.0347` n `229`; crypto_major avg `-0.145` n `8`; equity avg `0.4667` n `91`; fx avg `0.0022` n `6`; index avg `0.0307` n `25`; metal avg `0.0628` n `20`; unknown avg `-0.1216` n `766`
- 24h: commodity avg `-1.1202` n `12`; crypto_alt avg `1.0957` n `229`; crypto_major avg `1.6787` n `8`; equity avg `0.1292` n `91`; fx avg `-0.1147` n `6`; index avg `0.065` n `25`; metal avg `0.0338` n `20`; unknown avg `-0.1058` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
