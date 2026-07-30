# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T23:16:53.898555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `-0.0177` n `230`; crypto_major avg `-0.0257` n `8`; equity avg `-0.1422` n `102`; fx avg `0.0229` n `6`; index avg `-0.0308` n `25`; metal avg `-0.0358` n `20`; unknown avg `0.0003` n `779`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.0299` n `230`; crypto_major avg `0.0719` n `8`; equity avg `-0.0972` n `102`; fx avg `0.0062` n `6`; index avg `-0.0323` n `25`; metal avg `-0.0207` n `20`; unknown avg `-0.1622` n `779`
- 4h: commodity avg `0.0801` n `12`; crypto_alt avg `0.1347` n `230`; crypto_major avg `0.1504` n `8`; equity avg `0.9464` n `102`; fx avg `0.0605` n `6`; index avg `0.0678` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.3382` n `779`
- 24h: commodity avg `-0.0595` n `12`; crypto_alt avg `0.8149` n `230`; crypto_major avg `1.7089` n `8`; equity avg `7.4755` n `102`; fx avg `-0.395` n `6`; index avg `0.8328` n `25`; metal avg `0.4386` n `20`; unknown avg `0.0948` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
