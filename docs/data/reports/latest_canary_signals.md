# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T11:16:25.021227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.0156` n `230`; crypto_major avg `0.0111` n `8`; equity avg `0.0314` n `112`; fx avg `0.0005` n `6`; index avg `0.0068` n `25`; metal avg `0.0016` n `20`; unknown avg `-0.0099` n `784`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.0219` n `230`; crypto_major avg `0.0783` n `8`; equity avg `0.0739` n `112`; fx avg `-0.0143` n `6`; index avg `0.0038` n `25`; metal avg `-0.0284` n `20`; unknown avg `-0.0702` n `784`
- 4h: commodity avg `0.0662` n `12`; crypto_alt avg `0.1769` n `230`; crypto_major avg `0.2857` n `8`; equity avg `0.2149` n `112`; fx avg `-0.0099` n `6`; index avg `0.0122` n `25`; metal avg `0.0193` n `20`; unknown avg `1.294` n `784`
- 24h: commodity avg `0.2024` n `12`; crypto_alt avg `-0.0801` n `230`; crypto_major avg `0.0831` n `8`; equity avg `0.7293` n `112`; fx avg `-0.0408` n `6`; index avg `0.0348` n `25`; metal avg `0.0012` n `20`; unknown avg `1.063` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
