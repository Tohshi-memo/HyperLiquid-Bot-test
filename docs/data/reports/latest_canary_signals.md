# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T13:37:35.759480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `0.1996` n `234`; crypto_major avg `0.1488` n `8`; equity avg `-0.0891` n `141`; fx avg `-0.005` n `6`; index avg `-0.0365` n `26`; metal avg `0.0309` n `20`; unknown avg `12.7615` n `962`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.1992` n `234`; crypto_major avg `0.0166` n `8`; equity avg `-0.2045` n `141`; fx avg `-0.0258` n `6`; index avg `-0.0444` n `26`; metal avg `-0.042` n `20`; unknown avg `100.6509` n `960`
- 4h: commodity avg `-0.1655` n `12`; crypto_alt avg `1.5665` n `234`; crypto_major avg `1.3436` n `8`; equity avg `0.2963` n `141`; fx avg `-0.0188` n `6`; index avg `0.0388` n `26`; metal avg `0.0133` n `20`; unknown avg `198.4136` n `954`
- 24h: commodity avg `-0.252` n `12`; crypto_alt avg `-2.2571` n `234`; crypto_major avg `-1.7197` n `8`; equity avg `-2.6182` n `141`; fx avg `0.0013` n `6`; index avg `-0.2317` n `26`; metal avg `-0.9616` n `20`; unknown avg `5.5787` n `814`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
