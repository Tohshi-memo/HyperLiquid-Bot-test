# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T05:07:28.700479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `12`; crypto_alt avg `0.0488` n `230`; crypto_major avg `-0.009` n `8`; equity avg `-0.0379` n `113`; fx avg `-0.0099` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.0177` n `785`
- 1h: commodity avg `0.0671` n `12`; crypto_alt avg `-0.0843` n `230`; crypto_major avg `-0.0726` n `8`; equity avg `0.0023` n `113`; fx avg `-0.0176` n `6`; index avg `0.0031` n `25`; metal avg `-0.0917` n `20`; unknown avg `-0.0525` n `785`
- 4h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.0478` n `230`; crypto_major avg `0.2542` n `8`; equity avg `0.4973` n `113`; fx avg `0.0189` n `6`; index avg `0.1601` n `25`; metal avg `-0.08` n `20`; unknown avg `-0.0695` n `785`
- 24h: commodity avg `0.8921` n `12`; crypto_alt avg `-0.5538` n `230`; crypto_major avg `-0.4852` n `8`; equity avg `-0.825` n `113`; fx avg `0.0753` n `6`; index avg `0.0651` n `25`; metal avg `0.4005` n `20`; unknown avg `103.8405` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
