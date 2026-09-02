# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T10:22:27.344048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1706` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0696` n `12`; crypto_alt avg `0.0286` n `232`; crypto_major avg `0.107` n `8`; equity avg `0.0889` n `132`; fx avg `-0.0108` n `6`; index avg `0.0209` n `26`; metal avg `0.0566` n `20`; unknown avg `0.0837` n `792`
- 1h: commodity avg `-0.0641` n `12`; crypto_alt avg `-0.6085` n `232`; crypto_major avg `-0.3585` n `8`; equity avg `-0.1088` n `132`; fx avg `-0.0033` n `6`; index avg `-0.0055` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.0511` n `790`
- 4h: commodity avg `-0.1402` n `12`; crypto_alt avg `-1.0502` n `232`; crypto_major avg `-1.2439` n `8`; equity avg `-0.5588` n `132`; fx avg `-0.0349` n `6`; index avg `-0.0733` n `26`; metal avg `-0.0807` n `20`; unknown avg `-0.3456` n `788`
- 24h: commodity avg `0.5581` n `12`; crypto_alt avg `-0.9932` n `232`; crypto_major avg `-2.2172` n `8`; equity avg `-1.8948` n `130`; fx avg `-0.2137` n `6`; index avg `-0.3193` n `26`; metal avg `-0.5337` n `20`; unknown avg `-0.5058` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
