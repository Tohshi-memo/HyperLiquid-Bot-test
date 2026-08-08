# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T20:13:01.516645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `-0.0208` n `230`; crypto_major avg `0.0237` n `8`; equity avg `-0.0251` n `112`; fx avg `-0.0051` n `6`; index avg `0.0046` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.0107` n `784`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.0569` n `230`; crypto_major avg `0.1176` n `8`; equity avg `0.1101` n `112`; fx avg `-0.0014` n `6`; index avg `0.0127` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.077` n `784`
- 4h: commodity avg `0.1504` n `12`; crypto_alt avg `0.1263` n `230`; crypto_major avg `-0.1662` n `8`; equity avg `0.252` n `112`; fx avg `0.0034` n `6`; index avg `0.0093` n `25`; metal avg `0.009` n `20`; unknown avg `0.4229` n `784`
- 24h: commodity avg `0.1662` n `12`; crypto_alt avg `1.5223` n `230`; crypto_major avg `1.2055` n `8`; equity avg `0.6809` n `112`; fx avg `0.017` n `6`; index avg `0.0367` n `25`; metal avg `0.101` n `20`; unknown avg `0.2258` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
