# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T14:22:27.868427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1081` n `12`; crypto_alt avg `0.0479` n `232`; crypto_major avg `0.1049` n `8`; equity avg `0.2382` n `133`; fx avg `0.0114` n `6`; index avg `0.0553` n `26`; metal avg `-0.0245` n `20`; unknown avg `-0.0138` n `791`
- 1h: commodity avg `0.0268` n `12`; crypto_alt avg `0.6328` n `232`; crypto_major avg `0.89` n `8`; equity avg `0.5722` n `133`; fx avg `-0.0826` n `6`; index avg `0.1418` n `26`; metal avg `0.2783` n `20`; unknown avg `0.5155` n `789`
- 4h: commodity avg `-0.0395` n `12`; crypto_alt avg `0.5841` n `232`; crypto_major avg `0.9936` n `8`; equity avg `1.2058` n `133`; fx avg `-0.144` n `6`; index avg `0.2548` n `26`; metal avg `0.6582` n `20`; unknown avg `1.2334` n `789`
- 24h: commodity avg `0.6608` n `12`; crypto_alt avg `-1.0853` n `232`; crypto_major avg `-1.4186` n `8`; equity avg `-0.0226` n `132`; fx avg `-0.344` n `6`; index avg `-0.0421` n `26`; metal avg `0.1377` n `20`; unknown avg `0.1976` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
