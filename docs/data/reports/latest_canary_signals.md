# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T03:52:27.167171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `12`; crypto_alt avg `-0.0074` n `230`; crypto_major avg `0.0344` n `8`; equity avg `-0.0135` n `112`; fx avg `0.0019` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.2784` n `783`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `0.2403` n `230`; crypto_major avg `0.3788` n `8`; equity avg `-0.0217` n `112`; fx avg `0.008` n `6`; index avg `-0.0067` n `25`; metal avg `0.0091` n `20`; unknown avg `0.0718` n `783`
- 4h: commodity avg `0.0254` n `12`; crypto_alt avg `0.447` n `230`; crypto_major avg `0.5419` n `8`; equity avg `-0.0463` n `112`; fx avg `0.0067` n `6`; index avg `0.005` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0606` n `783`
- 24h: commodity avg `-0.1583` n `12`; crypto_alt avg `0.0653` n `230`; crypto_major avg `0.6355` n `8`; equity avg `1.6804` n `112`; fx avg `-0.0775` n `6`; index avg `0.2219` n `25`; metal avg `0.3507` n `20`; unknown avg `0.006` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
