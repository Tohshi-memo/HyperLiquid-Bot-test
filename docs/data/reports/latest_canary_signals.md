# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T16:52:36.699086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0745` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6504` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.215` n `13`; crypto_alt avg `-0.1343` n `235`; crypto_major avg `-0.0209` n `8`; equity avg `-0.1225` n `143`; fx avg `0.0137` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0009` n `20`; unknown avg `2.1271` n `984`
- 1h: commodity avg `0.1927` n `13`; crypto_alt avg `-0.2669` n `235`; crypto_major avg `-0.1098` n `8`; equity avg `-0.1221` n `143`; fx avg `0.0181` n `6`; index avg `-0.0105` n `26`; metal avg `0.0638` n `20`; unknown avg `2.1456` n `976`
- 4h: commodity avg `0.3769` n `13`; crypto_alt avg `-1.0601` n `235`; crypto_major avg `-1.6976` n `8`; equity avg `-0.3716` n `143`; fx avg `0.0783` n `6`; index avg `-0.0472` n `26`; metal avg `-0.5168` n `20`; unknown avg `0.8651` n `934`
- 24h: commodity avg `-0.0882` n `13`; crypto_alt avg `2.3288` n `235`; crypto_major avg `1.226` n `8`; equity avg `1.3944` n `142`; fx avg `-0.1037` n `6`; index avg `0.4498` n `26`; metal avg `-0.1859` n `20`; unknown avg `101.4453` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
