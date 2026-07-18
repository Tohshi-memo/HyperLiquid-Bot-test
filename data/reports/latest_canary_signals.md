# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T00:07:26.863993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `-0.0201` n `230`; crypto_major avg `-0.0344` n `8`; equity avg `0.0131` n `96`; fx avg `-0.0033` n `6`; index avg `-0.0235` n `25`; metal avg `0.0497` n `20`; unknown avg `-0.0309` n `769`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `0.1759` n `230`; crypto_major avg `0.1117` n `8`; equity avg `-0.0102` n `96`; fx avg `0.0018` n `6`; index avg `-0.0332` n `25`; metal avg `0.0464` n `20`; unknown avg `-0.1207` n `769`
- 4h: commodity avg `0.1129` n `12`; crypto_alt avg `0.0824` n `230`; crypto_major avg `-0.0413` n `8`; equity avg `0.0157` n `96`; fx avg `-0.0486` n `6`; index avg `-0.0451` n `25`; metal avg `0.0621` n `20`; unknown avg `-0.066` n `769`
- 24h: commodity avg `0.728` n `12`; crypto_alt avg `-0.2173` n `230`; crypto_major avg `-0.4363` n `8`; equity avg `-0.7573` n `94`; fx avg `0.0169` n `6`; index avg `-0.245` n `25`; metal avg `0.069` n `20`; unknown avg `0.1305` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
