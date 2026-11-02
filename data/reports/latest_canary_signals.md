# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T15:52:32.327601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `13`; crypto_alt avg `-0.1424` n `239`; crypto_major avg `-0.1947` n `8`; equity avg `-0.549` n `156`; fx avg `0.011` n `6`; index avg `-0.0457` n `27`; metal avg `0.0454` n `20`; unknown avg `-0.2904` n `1265`
- 1h: commodity avg `0.0719` n `13`; crypto_alt avg `-0.1032` n `239`; crypto_major avg `-0.234` n `8`; equity avg `0.629` n `156`; fx avg `0.02` n `6`; index avg `0.0593` n `27`; metal avg `0.0287` n `20`; unknown avg `15.2422` n `1257`
- 4h: commodity avg `-0.3795` n `13`; crypto_alt avg `0.0271` n `238`; crypto_major avg `-0.0608` n `8`; equity avg `-1.0258` n `156`; fx avg `0.0132` n `6`; index avg `0.0239` n `27`; metal avg `0.3665` n `20`; unknown avg `48.4576` n `1253`
- 24h: commodity avg `-0.8966` n `13`; crypto_alt avg `-1.9733` n `238`; crypto_major avg `-0.649` n `8`; equity avg `-0.2555` n `156`; fx avg `0.2706` n `6`; index avg `0.2634` n `27`; metal avg `0.3794` n `20`; unknown avg `7.3553` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
