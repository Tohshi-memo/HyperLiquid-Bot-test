# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T08:22:51.587629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `-0.0329` n `230`; crypto_major avg `-0.1073` n `8`; equity avg `0.0032` n `112`; fx avg `-0.0001` n `6`; index avg `-0.0073` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0126` n `785`
- 1h: commodity avg `0.0341` n `12`; crypto_alt avg `0.2198` n `230`; crypto_major avg `0.0519` n `8`; equity avg `-0.0043` n `112`; fx avg `0.0038` n `6`; index avg `0.0017` n `25`; metal avg `0.0245` n `20`; unknown avg `-0.0283` n `785`
- 4h: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.1664` n `230`; crypto_major avg `0.0619` n `8`; equity avg `0.0888` n `112`; fx avg `-0.0148` n `6`; index avg `-0.0012` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.045` n `752`
- 24h: commodity avg `0.2421` n `12`; crypto_alt avg `1.4521` n `230`; crypto_major avg `0.6023` n `8`; equity avg `0.6109` n `112`; fx avg `-0.0133` n `6`; index avg `0.0733` n `25`; metal avg `0.0297` n `20`; unknown avg `0.4319` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
