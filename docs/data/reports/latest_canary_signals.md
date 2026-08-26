# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T16:22:30.238666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0726` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4201` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0542` n `12`; crypto_alt avg `-0.3159` n `231`; crypto_major avg `-0.2567` n `8`; equity avg `0.0476` n `122`; fx avg `0.0016` n `6`; index avg `0.0063` n `25`; metal avg `-0.0234` n `20`; unknown avg `-0.0784` n `797`
- 1h: commodity avg `0.2905` n `12`; crypto_alt avg `-0.2732` n `231`; crypto_major avg `-0.1239` n `8`; equity avg `-0.1232` n `122`; fx avg `0.0146` n `6`; index avg `-0.0249` n `25`; metal avg `-0.1077` n `20`; unknown avg `0.0136` n `797`
- 4h: commodity avg `0.6213` n `12`; crypto_alt avg `-1.6627` n `231`; crypto_major avg `-1.4513` n `8`; equity avg `-0.2976` n `122`; fx avg `-0.0015` n `6`; index avg `-0.0312` n `25`; metal avg `-0.2701` n `20`; unknown avg `-0.1688` n `797`
- 24h: commodity avg `0.4683` n `12`; crypto_alt avg `-2.3744` n `231`; crypto_major avg `-2.1869` n `8`; equity avg `-0.5469` n `122`; fx avg `-0.0332` n `6`; index avg `-0.0142` n `25`; metal avg `-0.2769` n `20`; unknown avg `0.2816` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `669`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0963`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0854`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0698`, n `669`, weak_sample_signal
