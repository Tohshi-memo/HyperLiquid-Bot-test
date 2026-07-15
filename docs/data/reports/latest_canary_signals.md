# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T04:52:25.807246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `0.0534` n `230`; crypto_major avg `0.0546` n `8`; equity avg `-0.0651` n `93`; fx avg `-0.0047` n `6`; index avg `0.0039` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.1143` n `767`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.1427` n `230`; crypto_major avg `-0.0601` n `8`; equity avg `-0.0539` n `93`; fx avg `0.0077` n `6`; index avg `-0.0153` n `25`; metal avg `0.009` n `20`; unknown avg `-0.0808` n `767`
- 4h: commodity avg `-0.1292` n `12`; crypto_alt avg `-0.0508` n `230`; crypto_major avg `0.196` n `8`; equity avg `0.9215` n `93`; fx avg `0.0539` n `6`; index avg `0.0949` n `25`; metal avg `-0.1202` n `20`; unknown avg `-0.1877` n `767`
- 24h: commodity avg `0.0267` n `12`; crypto_alt avg `1.7987` n `230`; crypto_major avg `3.2942` n `8`; equity avg `2.34` n `92`; fx avg `0.1534` n `6`; index avg `0.6398` n `25`; metal avg `0.3547` n `20`; unknown avg `0.4118` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
