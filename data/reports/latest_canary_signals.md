# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T19:37:36.997125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0559` n `12`; crypto_alt avg `0.0721` n `228`; crypto_major avg `0.1329` n `8`; equity avg `0.1284` n `86`; fx avg `0.0057` n `6`; index avg `0.0037` n `23`; metal avg `-0.0456` n `20`; unknown avg `0.0282` n `765`
- 1h: commodity avg `0.0236` n `12`; crypto_alt avg `-0.2386` n `228`; crypto_major avg `-0.2466` n `8`; equity avg `-0.2459` n `86`; fx avg `0.0118` n `6`; index avg `-0.0592` n `23`; metal avg `-0.0306` n `20`; unknown avg `-0.2107` n `765`
- 4h: commodity avg `0.0976` n `12`; crypto_alt avg `-0.2917` n `228`; crypto_major avg `0.2457` n `8`; equity avg `-0.2092` n `86`; fx avg `0.0431` n `6`; index avg `-0.0209` n `23`; metal avg `-0.0657` n `20`; unknown avg `-0.1653` n `765`
- 24h: commodity avg `0.4953` n `12`; crypto_alt avg `-0.3778` n `228`; crypto_major avg `-0.2365` n `8`; equity avg `-0.0148` n `86`; fx avg `0.0855` n `6`; index avg `0.4012` n `23`; metal avg `0.7435` n `20`; unknown avg `0.4558` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
