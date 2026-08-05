# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T13:52:32.992520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.3042` n `230`; crypto_major avg `0.4153` n `8`; equity avg `0.7132` n `108`; fx avg `-0.0127` n `6`; index avg `0.0609` n `25`; metal avg `0.1036` n `20`; unknown avg `0.1394` n `782`
- 1h: commodity avg `-0.1986` n `12`; crypto_alt avg `-0.1942` n `230`; crypto_major avg `-0.1985` n `8`; equity avg `0.45` n `108`; fx avg `-0.0148` n `6`; index avg `0.0899` n `25`; metal avg `0.0868` n `20`; unknown avg `-0.07` n `782`
- 4h: commodity avg `-0.2386` n `12`; crypto_alt avg `-0.2105` n `230`; crypto_major avg `-0.1831` n `8`; equity avg `0.5393` n `108`; fx avg `-0.022` n `6`; index avg `0.1521` n `25`; metal avg `0.1072` n `20`; unknown avg `-0.0701` n `781`
- 24h: commodity avg `-0.0571` n `12`; crypto_alt avg `0.6206` n `230`; crypto_major avg `0.5027` n `8`; equity avg `1.8601` n `108`; fx avg `0.0623` n `6`; index avg `0.4388` n `25`; metal avg `0.6058` n `20`; unknown avg `0.6937` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
