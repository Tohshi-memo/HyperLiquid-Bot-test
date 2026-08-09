# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T08:37:25.477454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.022` n `230`; crypto_major avg `-0.0166` n `8`; equity avg `0.0457` n `112`; fx avg `-0.002` n `6`; index avg `-0.0048` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0377` n `785`
- 1h: commodity avg `0.0518` n `12`; crypto_alt avg `0.0592` n `230`; crypto_major avg `0.0091` n `8`; equity avg `0.0161` n `112`; fx avg `-0.0019` n `6`; index avg `-0.0059` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0277` n `785`
- 4h: commodity avg `0.0149` n `12`; crypto_alt avg `-0.1702` n `230`; crypto_major avg `0.0877` n `8`; equity avg `0.1244` n `112`; fx avg `-0.0167` n `6`; index avg `-0.0064` n `25`; metal avg `0.0236` n `20`; unknown avg `-0.0728` n `752`
- 24h: commodity avg `0.278` n `12`; crypto_alt avg `1.3199` n `230`; crypto_major avg `0.5061` n `8`; equity avg `0.6611` n `112`; fx avg `-0.0266` n `6`; index avg `0.0689` n `25`; metal avg `0.037` n `20`; unknown avg `0.2565` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
