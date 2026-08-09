# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T15:37:25.683003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `0.0982` n `230`; crypto_major avg `0.1284` n `8`; equity avg `-0.012` n `112`; fx avg `-0.0048` n `6`; index avg `-0.0038` n `25`; metal avg `0.01` n `20`; unknown avg `-0.0223` n `785`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `0.29` n `230`; crypto_major avg `0.2477` n `8`; equity avg `0.006` n `112`; fx avg `0.0011` n `6`; index avg `0.0047` n `25`; metal avg `0.0298` n `20`; unknown avg `-0.0221` n `785`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `0.63` n `230`; crypto_major avg `0.5184` n `8`; equity avg `0.1059` n `112`; fx avg `0.0055` n `6`; index avg `0.0177` n `25`; metal avg `0.0479` n `20`; unknown avg `0.0633` n `785`
- 24h: commodity avg `0.164` n `12`; crypto_alt avg `1.083` n `230`; crypto_major avg `0.2389` n `8`; equity avg `0.3287` n `112`; fx avg `-0.0048` n `6`; index avg `0.0037` n `25`; metal avg `0.0931` n `20`; unknown avg `0.4309` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
