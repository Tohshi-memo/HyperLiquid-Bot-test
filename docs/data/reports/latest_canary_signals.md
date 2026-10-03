# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T08:32:18.280237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `13`; crypto_alt avg `-0.0769` n `235`; crypto_major avg `-0.0444` n `8`; equity avg `-0.0044` n `143`; fx avg `0.0` n `6`; index avg `0.0016` n `26`; metal avg `-0.0079` n `20`; unknown avg `-0.0136` n `984`
- 1h: commodity avg `0.0208` n `13`; crypto_alt avg `-0.1594` n `235`; crypto_major avg `-0.1101` n `8`; equity avg `-0.0002` n `143`; fx avg `-0.0004` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.0581` n `966`
- 4h: commodity avg `-0.005` n `13`; crypto_alt avg `-0.313` n `235`; crypto_major avg `0.0049` n `8`; equity avg `0.0225` n `143`; fx avg `-0.001` n `6`; index avg `-0.003` n `26`; metal avg `0.0088` n `20`; unknown avg `0.0736` n `944`
- 24h: commodity avg `0.6792` n `13`; crypto_alt avg `-2.8076` n `235`; crypto_major avg `-2.6739` n `8`; equity avg `-0.0562` n `142`; fx avg `0.0321` n `6`; index avg `0.121` n `26`; metal avg `-0.3769` n `20`; unknown avg `-0.4409` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
