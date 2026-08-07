# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T20:52:29.435964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.0345` n `230`; crypto_major avg `-0.0146` n `8`; equity avg `0.0356` n `112`; fx avg `-0.004` n `6`; index avg `-0.0016` n `25`; metal avg `0.0317` n `20`; unknown avg `0.0815` n `782`
- 1h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.2513` n `230`; crypto_major avg `-0.0947` n `8`; equity avg `0.1624` n `112`; fx avg `0.0095` n `6`; index avg `0.0021` n `25`; metal avg `-0.0465` n `20`; unknown avg `0.0897` n `782`
- 4h: commodity avg `-0.2417` n `12`; crypto_alt avg `-0.2932` n `230`; crypto_major avg `-0.1338` n `8`; equity avg `0.3178` n `112`; fx avg `-0.0063` n `6`; index avg `0.0469` n `25`; metal avg `0.0669` n `20`; unknown avg `-0.0745` n `782`
- 24h: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.2047` n `230`; crypto_major avg `-0.0265` n `8`; equity avg `2.1314` n `112`; fx avg `-0.154` n `6`; index avg `0.1151` n `25`; metal avg `0.3519` n `20`; unknown avg `0.0148` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
