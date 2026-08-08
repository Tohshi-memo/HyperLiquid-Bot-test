# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T11:52:29.592224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.0194` n `230`; crypto_major avg `0.0436` n `8`; equity avg `-0.0175` n `112`; fx avg `0.0053` n `6`; index avg `-0.0022` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0059` n `784`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `0.0031` n `230`; crypto_major avg `0.0561` n `8`; equity avg `0.0331` n `112`; fx avg `0.0111` n `6`; index avg `0.0203` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.0076` n `784`
- 4h: commodity avg `0.0415` n `12`; crypto_alt avg `0.2681` n `230`; crypto_major avg `0.3299` n `8`; equity avg `0.1875` n `112`; fx avg `-0.0018` n `6`; index avg `0.0385` n `25`; metal avg `0.0021` n `20`; unknown avg `1.2417` n `784`
- 24h: commodity avg `0.2035` n `12`; crypto_alt avg `0.1367` n `230`; crypto_major avg `0.2116` n `8`; equity avg `0.811` n `112`; fx avg `-0.0339` n `6`; index avg `0.0452` n `25`; metal avg `0.0408` n `20`; unknown avg `1.0794` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
