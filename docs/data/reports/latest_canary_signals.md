# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T20:22:34.497035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0627` n `233`; crypto_major avg `-0.0064` n `8`; equity avg `0.0879` n `134`; fx avg `-0.0036` n `6`; index avg `0.0101` n `26`; metal avg `0.041` n `20`; unknown avg `2.3794` n `773`
- 1h: commodity avg `0.0503` n `12`; crypto_alt avg `0.0067` n `233`; crypto_major avg `-0.1002` n `8`; equity avg `-0.2293` n `134`; fx avg `0.0034` n `6`; index avg `-0.0431` n `26`; metal avg `-0.0637` n `20`; unknown avg `0.9117` n `771`
- 4h: commodity avg `0.3661` n `12`; crypto_alt avg `-0.6855` n `233`; crypto_major avg `-0.2028` n `8`; equity avg `-0.4112` n `134`; fx avg `-0.0489` n `6`; index avg `-0.0784` n `26`; metal avg `-0.1893` n `20`; unknown avg `0.8404` n `749`
- 24h: commodity avg `0.0404` n `12`; crypto_alt avg `-0.1342` n `232`; crypto_major avg `-0.0382` n `8`; equity avg `0.3446` n `134`; fx avg `-0.0918` n `6`; index avg `-0.1621` n `26`; metal avg `-0.2945` n `20`; unknown avg `22.8826` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
