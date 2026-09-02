# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T03:07:28.628642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.3016` n `232`; crypto_major avg `0.2067` n `8`; equity avg `-0.0446` n `132`; fx avg `-0.0073` n `6`; index avg `-0.0161` n `26`; metal avg `-0.0432` n `20`; unknown avg `0.0758` n `790`
- 1h: commodity avg `-0.035` n `12`; crypto_alt avg `1.0856` n `232`; crypto_major avg `0.6636` n `8`; equity avg `0.1071` n `132`; fx avg `-0.0183` n `6`; index avg `0.0143` n `26`; metal avg `0.0421` n `20`; unknown avg `0.3724` n `790`
- 4h: commodity avg `0.0431` n `12`; crypto_alt avg `0.6706` n `232`; crypto_major avg `0.2226` n `8`; equity avg `-0.1567` n `132`; fx avg `-0.0837` n `6`; index avg `-0.0272` n `26`; metal avg `-0.2113` n `20`; unknown avg `-0.2693` n `790`
- 24h: commodity avg `0.8773` n `12`; crypto_alt avg `-0.353` n `232`; crypto_major avg `-1.5113` n `8`; equity avg `-2.2726` n `130`; fx avg `-0.0419` n `6`; index avg `-0.4065` n `26`; metal avg `-1.0886` n `20`; unknown avg `-0.4517` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0398`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0392`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0315`, n `668`, weak_sample_signal
