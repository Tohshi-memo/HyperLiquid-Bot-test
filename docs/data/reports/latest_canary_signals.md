# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T18:52:13.620024+00:00`
- Correlation status: `ready`
- Asset price records: `671`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0658` n `12`; crypto_alt avg `-0.0443` n `228`; crypto_major avg `0.0736` n `8`; equity avg `-0.0343` n `65`; fx avg `0.0102` n `5`; index avg `-0.007` n `23`; metal avg `-0.0528` n `18`; unknown avg `-0.2065` n `375`
- 1h: commodity avg `-0.246` n `12`; crypto_alt avg `0.4861` n `228`; crypto_major avg `0.4903` n `8`; equity avg `0.3738` n `65`; fx avg `0.0203` n `5`; index avg `0.036` n `23`; metal avg `0.1098` n `18`; unknown avg `0.0209` n `375`
- 4h: commodity avg `-0.2806` n `12`; crypto_alt avg `1.7152` n `228`; crypto_major avg `1.3772` n `8`; equity avg `0.6918` n `65`; fx avg `0.0124` n `5`; index avg `0.3295` n `23`; metal avg `0.0381` n `18`; unknown avg `-0.052` n `375`
- 24h: commodity avg `-0.049` n `12`; crypto_alt avg `3.4102` n `228`; crypto_major avg `1.6445` n `8`; equity avg `3.3372` n `65`; fx avg `0.1755` n `5`; index avg `1.6718` n `23`; metal avg `1.0407` n `18`; unknown avg `0.3057` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1229`, n `663`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `663`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1083`, n `667`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `667`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0935`, n `663`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `663`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `667`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0652`, n `667`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `663`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0582`, n `663`, weak_sample_signal
