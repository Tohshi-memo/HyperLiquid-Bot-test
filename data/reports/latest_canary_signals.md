# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T17:22:24.850065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `13`; crypto_alt avg `-0.1594` n `235`; crypto_major avg `-0.0595` n `8`; equity avg `-0.0008` n `144`; fx avg `0.0076` n `6`; index avg `-0.0012` n `26`; metal avg `0.0013` n `20`; unknown avg `0.2397` n `1078`
- 1h: commodity avg `0.0715` n `13`; crypto_alt avg `-0.0066` n `235`; crypto_major avg `0.1464` n `8`; equity avg `0.0186` n `144`; fx avg `-0.001` n `6`; index avg `-0.0006` n `26`; metal avg `0.0009` n `20`; unknown avg `0.3339` n `1076`
- 4h: commodity avg `-0.067` n `13`; crypto_alt avg `-0.1882` n `235`; crypto_major avg `0.1745` n `8`; equity avg `0.0328` n `144`; fx avg `0.0089` n `6`; index avg `-0.0191` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.139` n `1070`
- 24h: commodity avg `-0.0746` n `13`; crypto_alt avg `0.4458` n `235`; crypto_major avg `0.7045` n `8`; equity avg `0.2217` n `144`; fx avg `0.022` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.0542` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
