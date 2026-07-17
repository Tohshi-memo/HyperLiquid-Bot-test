# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T11:37:25.665630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.0702` n `230`; crypto_major avg `0.1167` n `8`; equity avg `0.1149` n `96`; fx avg `0.0126` n `6`; index avg `0.02` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0378` n `769`
- 1h: commodity avg `0.0635` n `12`; crypto_alt avg `-0.0809` n `230`; crypto_major avg `-0.0219` n `8`; equity avg `-0.2123` n `96`; fx avg `0.0161` n `6`; index avg `-0.0372` n `25`; metal avg `-0.0755` n `20`; unknown avg `0.0581` n `769`
- 4h: commodity avg `0.2702` n `12`; crypto_alt avg `0.4366` n `230`; crypto_major avg `0.6366` n `8`; equity avg `0.6945` n `96`; fx avg `0.0312` n `6`; index avg `0.0638` n `25`; metal avg `0.0047` n `20`; unknown avg `0.1095` n `768`
- 24h: commodity avg `0.1094` n `12`; crypto_alt avg `-1.3819` n `230`; crypto_major avg `-2.4678` n `8`; equity avg `-4.3128` n `94`; fx avg `-0.0017` n `6`; index avg `-0.5698` n `25`; metal avg `-0.7309` n `20`; unknown avg `-0.2678` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
