# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T11:29:45.608302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6848` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5655` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1431` n `12`; crypto_alt avg `0.0728` n `232`; crypto_major avg `-0.0379` n `8`; equity avg `0.3341` n `132`; fx avg `-0.0269` n `6`; index avg `0.0748` n `26`; metal avg `0.1387` n `20`; unknown avg `0.4216` n `792`
- 1h: commodity avg `-0.1306` n `12`; crypto_alt avg `-0.2939` n `232`; crypto_major avg `-0.2946` n `8`; equity avg `0.1077` n `132`; fx avg `-0.0454` n `6`; index avg `0.0474` n `26`; metal avg `0.1495` n `20`; unknown avg `0.5718` n `790`
- 4h: commodity avg `-0.1685` n `12`; crypto_alt avg `-1.5756` n `232`; crypto_major avg `-1.6456` n `8`; equity avg `-0.6198` n `132`; fx avg `-0.0668` n `6`; index avg `-0.0801` n `26`; metal avg `0.0392` n `20`; unknown avg `0.2932` n `790`
- 24h: commodity avg `0.4556` n `12`; crypto_alt avg `-1.5667` n `232`; crypto_major avg `-2.6002` n `8`; equity avg `-1.5822` n `130`; fx avg `-0.2678` n `6`; index avg `-0.2368` n `26`; metal avg `-0.2744` n `20`; unknown avg `0.0296` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
