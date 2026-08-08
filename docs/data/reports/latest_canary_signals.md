# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T07:32:50.486373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.0325` n `8`; equity avg `-0.0202` n `112`; fx avg `0.0005` n `6`; index avg `-0.0` n `25`; metal avg `0.0153` n `20`; unknown avg `-0.0036` n `784`
- 1h: commodity avg `0.0105` n `12`; crypto_alt avg `0.0021` n `230`; crypto_major avg `-0.0335` n `8`; equity avg `0.0281` n `112`; fx avg `-0.0064` n `6`; index avg `0.0053` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.0946` n `784`
- 4h: commodity avg `0.0188` n `12`; crypto_alt avg `0.0597` n `230`; crypto_major avg `0.0446` n `8`; equity avg `-0.0952` n `112`; fx avg `-0.0046` n `6`; index avg `-0.0422` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.1155` n `751`
- 24h: commodity avg `-0.2123` n `12`; crypto_alt avg `-0.0673` n `230`; crypto_major avg `0.613` n `8`; equity avg `1.1211` n `112`; fx avg `-0.0569` n `6`; index avg `0.0736` n `25`; metal avg `0.0728` n `20`; unknown avg `0.0277` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
