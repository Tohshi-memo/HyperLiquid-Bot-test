# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T05:52:33.491428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0543` n `12`; crypto_alt avg `0.003` n `230`; crypto_major avg `-0.0396` n `8`; equity avg `0.0839` n `107`; fx avg `0.0223` n `6`; index avg `0.0217` n `25`; metal avg `0.0034` n `20`; unknown avg `0.0911` n `781`
- 1h: commodity avg `-0.0391` n `12`; crypto_alt avg `-0.2214` n `230`; crypto_major avg `-0.2958` n `8`; equity avg `0.3611` n `107`; fx avg `0.0154` n `6`; index avg `0.0997` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0748` n `781`
- 4h: commodity avg `0.0484` n `12`; crypto_alt avg `-0.1025` n `230`; crypto_major avg `-0.0958` n `8`; equity avg `0.2859` n `107`; fx avg `0.0838` n `6`; index avg `0.036` n `25`; metal avg `0.087` n `20`; unknown avg `4.4757` n `780`
- 24h: commodity avg `0.2892` n `12`; crypto_alt avg `0.9598` n `230`; crypto_major avg `1.0793` n `8`; equity avg `2.1454` n `107`; fx avg `0.0666` n `6`; index avg `0.2385` n `25`; metal avg `0.0655` n `20`; unknown avg `0.147` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
