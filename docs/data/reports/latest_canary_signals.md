# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T12:52:33.465524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.2247` n `235`; crypto_major avg `-0.0787` n `8`; equity avg `-0.0959` n `144`; fx avg `-0.0029` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0664` n `20`; unknown avg `0.7064` n `1079`
- 1h: commodity avg `-0.0041` n `13`; crypto_alt avg `-0.3793` n `235`; crypto_major avg `-0.3226` n `8`; equity avg `-0.0481` n `144`; fx avg `-0.0107` n `6`; index avg `-0.0356` n `26`; metal avg `-0.0133` n `20`; unknown avg `0.6994` n `1071`
- 4h: commodity avg `-0.0571` n `13`; crypto_alt avg `-0.2824` n `235`; crypto_major avg `-0.4397` n `8`; equity avg `-0.1967` n `144`; fx avg `0.0108` n `6`; index avg `-0.027` n `26`; metal avg `-0.0826` n `20`; unknown avg `44.2714` n `1071`
- 24h: commodity avg `-0.2254` n `13`; crypto_alt avg `0.7654` n `235`; crypto_major avg `0.789` n `8`; equity avg `0.0028` n `144`; fx avg `-0.0489` n `6`; index avg `-0.0774` n `26`; metal avg `0.2377` n `20`; unknown avg `0.8201` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2141`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
