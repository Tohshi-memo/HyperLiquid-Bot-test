# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T11:37:29.838547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0373` n `12`; crypto_alt avg `0.0038` n `230`; crypto_major avg `-0.0087` n `8`; equity avg `0.0096` n `112`; fx avg `-0.0073` n `6`; index avg `0.0043` n `25`; metal avg `-0.0054` n `20`; unknown avg `-0.005` n `785`
- 1h: commodity avg `-0.0915` n `12`; crypto_alt avg `0.1458` n `230`; crypto_major avg `0.0076` n `8`; equity avg `0.0103` n `112`; fx avg `-0.0011` n `6`; index avg `-0.0012` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0118` n `785`
- 4h: commodity avg `0.0093` n `12`; crypto_alt avg `0.0459` n `230`; crypto_major avg `0.0542` n `8`; equity avg `-0.0728` n `112`; fx avg `-0.0051` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.0059` n `785`
- 24h: commodity avg `0.1803` n `12`; crypto_alt avg `1.1874` n `230`; crypto_major avg `0.332` n `8`; equity avg `0.3957` n `112`; fx avg `-0.0111` n `6`; index avg `0.027` n `25`; metal avg `0.0214` n `20`; unknown avg `0.2833` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
