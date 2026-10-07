# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T09:52:30.534684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.077` n `13`; crypto_alt avg `-0.2645` n `235`; crypto_major avg `-0.0982` n `8`; equity avg `-0.0509` n `150`; fx avg `0.0136` n `6`; index avg `-0.0164` n `26`; metal avg `0.0008` n `20`; unknown avg `0.2029` n `1076`
- 1h: commodity avg `0.1274` n `13`; crypto_alt avg `-0.8126` n `235`; crypto_major avg `-0.6009` n `8`; equity avg `-0.3537` n `150`; fx avg `-0.0035` n `6`; index avg `-0.0587` n `26`; metal avg `-0.1229` n `20`; unknown avg `0.2618` n `1074`
- 4h: commodity avg `0.1579` n `13`; crypto_alt avg `-1.1684` n `235`; crypto_major avg `-0.7788` n `8`; equity avg `-0.7659` n `150`; fx avg `-0.0921` n `6`; index avg `-0.1212` n `26`; metal avg `-0.316` n `20`; unknown avg `0.8975` n `1036`
- 24h: commodity avg `1.1974` n `13`; crypto_alt avg `-4.4898` n `235`; crypto_major avg `-2.9207` n `8`; equity avg `-0.9859` n `150`; fx avg `-0.0862` n `6`; index avg `-0.2013` n `26`; metal avg `-0.4597` n `20`; unknown avg `815.4986` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
