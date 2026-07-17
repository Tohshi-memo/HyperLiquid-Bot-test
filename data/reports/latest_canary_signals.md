# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T21:22:27.846287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0372` n `12`; crypto_alt avg `0.046` n `230`; crypto_major avg `-0.0064` n `8`; equity avg `-0.008` n `96`; fx avg `0.0` n `6`; index avg `0.0028` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0049` n `769`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `0.0423` n `230`; crypto_major avg `0.0971` n `8`; equity avg `0.0147` n `96`; fx avg `-0.013` n `6`; index avg `0.0012` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0109` n `769`
- 4h: commodity avg `0.0835` n `12`; crypto_alt avg `-0.3844` n `230`; crypto_major avg `-0.0735` n `8`; equity avg `-1.3681` n `96`; fx avg `-0.0285` n `6`; index avg `-0.1983` n `25`; metal avg `-0.0676` n `20`; unknown avg `-0.1893` n `769`
- 24h: commodity avg `0.6601` n `12`; crypto_alt avg `-1.3018` n `230`; crypto_major avg `-1.1994` n `8`; equity avg `-1.4772` n `94`; fx avg `0.0671` n `6`; index avg `-0.313` n `25`; metal avg `-0.0238` n `20`; unknown avg `-0.0711` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
