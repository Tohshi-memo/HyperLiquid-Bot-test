# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T14:37:59.445270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.0807` n `230`; crypto_major avg `-0.1274` n `8`; equity avg `-0.5067` n `108`; fx avg `0.0013` n `6`; index avg `-0.0542` n `25`; metal avg `-0.0427` n `20`; unknown avg `-0.0174` n `782`
- 1h: commodity avg `-0.2173` n `12`; crypto_alt avg `0.3155` n `230`; crypto_major avg `0.4653` n `8`; equity avg `-0.1308` n `108`; fx avg `-0.0025` n `6`; index avg `-0.0571` n `25`; metal avg `0.2042` n `20`; unknown avg `0.146` n `782`
- 4h: commodity avg `-0.3873` n `12`; crypto_alt avg `-0.1607` n `230`; crypto_major avg `-0.028` n `8`; equity avg `-0.2984` n `108`; fx avg `-0.0163` n `6`; index avg `0.0338` n `25`; metal avg `0.2773` n `20`; unknown avg `-0.0798` n `782`
- 24h: commodity avg `-0.325` n `12`; crypto_alt avg `0.8523` n `230`; crypto_major avg `0.5189` n `8`; equity avg `0.897` n `108`; fx avg `0.0377` n `6`; index avg `0.2949` n `25`; metal avg `0.8159` n `20`; unknown avg `0.7058` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
