# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T00:07:31.580624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `0.0305` n `8`; equity avg `0.0148` n `96`; fx avg `0.0034` n `6`; index avg `-0.0118` n `25`; metal avg `0.0109` n `20`; unknown avg `0.2752` n `770`
- 1h: commodity avg `-0.1006` n `12`; crypto_alt avg `0.0513` n `230`; crypto_major avg `0.0908` n `8`; equity avg `0.0417` n `96`; fx avg `-0.0005` n `6`; index avg `-0.0076` n `25`; metal avg `0.0257` n `20`; unknown avg `0.1195` n `770`
- 4h: commodity avg `-0.049` n `12`; crypto_alt avg `0.2785` n `230`; crypto_major avg `0.2667` n `8`; equity avg `0.0562` n `96`; fx avg `0.0087` n `6`; index avg `-0.008` n `25`; metal avg `0.0139` n `20`; unknown avg `0.3892` n `770`
- 24h: commodity avg `0.27` n `12`; crypto_alt avg `-0.239` n `230`; crypto_major avg `0.6651` n `8`; equity avg `-0.1852` n `96`; fx avg `-0.0719` n `6`; index avg `0.073` n `25`; metal avg `-0.07` n `20`; unknown avg `0.081` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
