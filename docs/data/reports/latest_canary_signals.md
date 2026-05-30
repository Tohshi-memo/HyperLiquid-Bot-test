# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T02:22:17.239682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1799` n `12`; crypto_alt avg `-0.0734` n `228`; crypto_major avg `-0.028` n `8`; equity avg `-0.0253` n `69`; fx avg `-0.0006` n `6`; index avg `-0.008` n `23`; metal avg `-0.0075` n `18`; unknown avg `-0.1752` n `419`
- 1h: commodity avg `-0.0831` n `12`; crypto_alt avg `0.4608` n `228`; crypto_major avg `0.4248` n `8`; equity avg `0.0503` n `69`; fx avg `0.0015` n `6`; index avg `-0.0623` n `23`; metal avg `0.0143` n `18`; unknown avg `-0.1089` n `419`
- 4h: commodity avg `0.0666` n `12`; crypto_alt avg `1.4494` n `228`; crypto_major avg `1.0868` n `8`; equity avg `0.2284` n `69`; fx avg `-0.0119` n `6`; index avg `-0.0315` n `23`; metal avg `0.0394` n `18`; unknown avg `-0.5456` n `419`
- 24h: commodity avg `-0.229` n `12`; crypto_alt avg `1.8871` n `228`; crypto_major avg `2.3458` n `8`; equity avg `1.2227` n `69`; fx avg `0.1009` n `6`; index avg `0.1601` n `23`; metal avg `-0.087` n `18`; unknown avg `0.5547` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
