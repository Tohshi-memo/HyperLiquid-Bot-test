# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T06:07:23.499051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.0197` n `230`; crypto_major avg `0.0469` n `8`; equity avg `0.1041` n `114`; fx avg `0.0082` n `6`; index avg `0.0216` n `25`; metal avg `0.0388` n `20`; unknown avg `0.0463` n `776`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `-0.0885` n `230`; crypto_major avg `0.0435` n `8`; equity avg `0.269` n `114`; fx avg `0.0147` n `6`; index avg `0.0563` n `25`; metal avg `0.1085` n `20`; unknown avg `0.0246` n `776`
- 4h: commodity avg `-0.2095` n `12`; crypto_alt avg `0.4556` n `230`; crypto_major avg `0.5268` n `8`; equity avg `0.9314` n `114`; fx avg `0.0398` n `6`; index avg `0.1225` n `25`; metal avg `0.0728` n `20`; unknown avg `0.1044` n `776`
- 24h: commodity avg `-0.2335` n `12`; crypto_alt avg `0.3153` n `230`; crypto_major avg `0.775` n `8`; equity avg `1.0684` n `114`; fx avg `-0.012` n `6`; index avg `0.1433` n `25`; metal avg `0.2759` n `20`; unknown avg `0.0582` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
