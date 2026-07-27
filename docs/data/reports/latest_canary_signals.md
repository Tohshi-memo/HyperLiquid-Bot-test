# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T11:22:27.343875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0252` n `230`; crypto_major avg `-0.0252` n `8`; equity avg `-0.0679` n `100`; fx avg `-0.0014` n `6`; index avg `-0.0149` n `25`; metal avg `0.0131` n `20`; unknown avg `0.0434` n `776`
- 1h: commodity avg `0.1106` n `12`; crypto_alt avg `-0.0847` n `230`; crypto_major avg `-0.0582` n `8`; equity avg `-0.2337` n `100`; fx avg `-0.0129` n `6`; index avg `-0.0273` n `25`; metal avg `0.0204` n `20`; unknown avg `-0.0232` n `775`
- 4h: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.4494` n `230`; crypto_major avg `-0.1659` n `8`; equity avg `-0.1287` n `100`; fx avg `-0.0276` n `6`; index avg `-0.007` n `25`; metal avg `-0.0701` n `20`; unknown avg `-0.1762` n `775`
- 24h: commodity avg `-0.576` n `12`; crypto_alt avg `0.5124` n `230`; crypto_major avg `1.2407` n `8`; equity avg `1.0744` n `100`; fx avg `0.0897` n `6`; index avg `0.1348` n `25`; metal avg `0.3507` n `20`; unknown avg `-0.1491` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
