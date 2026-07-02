# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T03:37:34.433874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.2228` n `228`; crypto_major avg `0.428` n `8`; equity avg `0.0574` n `88`; fx avg `-0.0011` n `6`; index avg `0.0098` n `25`; metal avg `0.029` n `20`; unknown avg `3.6775` n `763`
- 1h: commodity avg `-0.0455` n `12`; crypto_alt avg `0.1349` n `228`; crypto_major avg `0.2332` n `8`; equity avg `-0.1918` n `88`; fx avg `-0.0002` n `6`; index avg `-0.0501` n `25`; metal avg `0.0759` n `20`; unknown avg `4.6531` n `763`
- 4h: commodity avg `-0.1197` n `12`; crypto_alt avg `0.9224` n `228`; crypto_major avg `0.7152` n `8`; equity avg `0.0803` n `88`; fx avg `-0.0025` n `6`; index avg `0.0331` n `25`; metal avg `0.4101` n `20`; unknown avg `-0.2253` n `761`
- 24h: commodity avg `-0.6864` n `12`; crypto_alt avg `1.6829` n `228`; crypto_major avg `0.9488` n `8`; equity avg `-1.3583` n `88`; fx avg `-0.0429` n `6`; index avg `-0.3365` n `25`; metal avg `1.0601` n `20`; unknown avg `25.1148` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
