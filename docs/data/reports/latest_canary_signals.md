# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T16:22:25.243994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6055` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0574` n `12`; crypto_alt avg `0.1081` n `230`; crypto_major avg `0.2579` n `8`; equity avg `0.055` n `121`; fx avg `-0.0029` n `6`; index avg `-0.0189` n `25`; metal avg `0.0139` n `20`; unknown avg `1.1707` n `793`
- 1h: commodity avg `-0.0833` n `12`; crypto_alt avg `-0.4323` n `230`; crypto_major avg `-0.5964` n `8`; equity avg `0.0919` n `121`; fx avg `0.0129` n `6`; index avg `0.0382` n `25`; metal avg `0.0906` n `20`; unknown avg `1.212` n `793`
- 4h: commodity avg `-0.0843` n `12`; crypto_alt avg `1.1146` n `230`; crypto_major avg `1.2781` n `8`; equity avg `-0.3274` n `121`; fx avg `-0.0174` n `6`; index avg `-0.0496` n `25`; metal avg `0.0161` n `20`; unknown avg `1.3651` n `793`
- 24h: commodity avg `0.1611` n `12`; crypto_alt avg `7.5447` n `230`; crypto_major avg `4.8396` n `8`; equity avg `1.3541` n `121`; fx avg `-0.1151` n `6`; index avg `0.1058` n `25`; metal avg `0.6138` n `20`; unknown avg `3.3904` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
