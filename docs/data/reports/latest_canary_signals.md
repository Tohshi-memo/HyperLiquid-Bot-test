# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T23:52:23.698570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `12`; crypto_alt avg `0.1264` n `230`; crypto_major avg `0.1105` n `8`; equity avg `-0.0405` n `92`; fx avg `0.0011` n `6`; index avg `-0.0117` n `25`; metal avg `0.0523` n `20`; unknown avg `0.0569` n `766`
- 1h: commodity avg `-0.0272` n `12`; crypto_alt avg `0.1972` n `230`; crypto_major avg `0.2211` n `8`; equity avg `-0.1239` n `92`; fx avg `0.0124` n `6`; index avg `-0.0068` n `25`; metal avg `0.0239` n `20`; unknown avg `0.001` n `765`
- 4h: commodity avg `-0.2165` n `12`; crypto_alt avg `-0.973` n `230`; crypto_major avg `-0.9126` n `8`; equity avg `-0.4912` n `92`; fx avg `-0.0483` n `6`; index avg `-0.1056` n `25`; metal avg `-0.2016` n `20`; unknown avg `0.3066` n `765`
- 24h: commodity avg `0.049` n `12`; crypto_alt avg `-0.6807` n `230`; crypto_major avg `-0.1795` n `8`; equity avg `-0.4589` n `92`; fx avg `-0.0587` n `6`; index avg `-0.0898` n `25`; metal avg `-0.2815` n `20`; unknown avg `0.2987` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
