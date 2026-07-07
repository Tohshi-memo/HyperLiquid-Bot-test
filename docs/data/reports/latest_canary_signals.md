# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T21:52:30.853139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1234` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.5109` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `-0.0172` n `229`; crypto_major avg `0.0417` n `8`; equity avg `0.0046` n `91`; fx avg `-0.0038` n `6`; index avg `0.0065` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.0069` n `763`
- 1h: commodity avg `0.0523` n `12`; crypto_alt avg `-0.3026` n `229`; crypto_major avg `-0.3997` n `8`; equity avg `-0.2835` n `91`; fx avg `-0.0131` n `6`; index avg `-0.0179` n `25`; metal avg `0.0423` n `20`; unknown avg `-0.055` n `763`
- 4h: commodity avg `0.4676` n `12`; crypto_alt avg `-1.5957` n `229`; crypto_major avg `-1.6558` n `8`; equity avg `-0.9493` n `91`; fx avg `-0.0207` n `6`; index avg `-0.1449` n `25`; metal avg `-0.3879` n `20`; unknown avg `1.0646` n `761`
- 24h: commodity avg `0.9559` n `12`; crypto_alt avg `-3.0721` n `229`; crypto_major avg `-2.4394` n `8`; equity avg `-3.5281` n `91`; fx avg `-0.2922` n `6`; index avg `-0.6357` n `25`; metal avg `-0.5764` n `20`; unknown avg `-0.4672` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
